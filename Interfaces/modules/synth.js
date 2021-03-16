debug = false

zyn_port = 10000
bcr_port = 12345
zyn_selected = 0
midi_port = 'keyboards'

bcr_scenes = {
    0: 8,
    1: 9,
    2: 12,
    3: 12,
    4: 14,
    5: 15,
    6: 19
}

state = {}
tmpstate = {}
statesave = false
for (var i in bcr_scenes){
    state[parseInt(i)] = {}
    tmpstate[parseInt(i)] = {}
}


function midiSteps(steps) {
    return (v)=>{
        return parseInt(127*v/steps)
    }
}

bcr_mapping = {
    '/kit0/adpars/GlobalPar/GlobalFilter/Pfreq': {control: 1},
    '/kit0/adpars/GlobalPar/GlobalFilter/Pcenterfreq': {control: 1},
    '/kit0/adpars/GlobalPar/GlobalFilter/Pnumformants': {control: 4, map: midiSteps(12)},
    '/kit0/adpars/GlobalPar/GlobalFilter/Poctavesfreq': {control: 5},
    '/kit0/adpars/GlobalPar/GlobalFilter/Pq': {control: 2},
    '/kit0/adpars/GlobalPar/GlobalFilter/Pstages': {control: 3, map: midiSteps(5)},
    '/kit0/adpars/GlobalPar/PBandwidth': {control: 6},
    '/kit0/adpars/GlobalPar/PCoarseDetune': {control: 7},
    '/partefx1/EQ/filter0/Pfreq': {control: 8, type: 'f'},
    '/kit0/adpars/GlobalPar/GlobalFilter/Ptype': {control: 33, forcefeedback: true},
    '/kit0/adpars/GlobalPar/octave': {control: 41, map: v=>v+2, forcefeedback: true},
    '/kit0/adpars/GlobalPar/AmpEnvelope/PA_dt': {control: 49},
    '/kit0/adpars/GlobalPar/AmpEnvelope/PD_dt': {control: 50},
    '/kit0/adpars/GlobalPar/AmpEnvelope/PS_val': {control: 51},
    '/kit0/adpars/GlobalPar/AmpEnvelope/PR_dt': {control: 52},
    '/kit0/adpars/GlobalPar/AmpLfo/Pfreq': {control: 53, map: v=>parseInt(127*v), type: 'f', forcefeedback: true, action: ()=>{send('127.0.0.1', zyn_port, `/part${zyn_selected}/kit0/adpars/GlobalPar/AmpLfo/Pstartphase`, {type: 'i', value:0})}},
    '/kit0/adpars/GlobalPar/AmpLfo/Pintensity': {control: 54},
    '/kit0/adpars/GlobalPar/AmpLfo/PLFOtype': {control: 56, map: midiSteps(8)},
    '/kit0/adpars/GlobalPar/FreqEnvelope/PA_val': {control: 57},
    '/kit0/adpars/GlobalPar/FreqEnvelope/PA_dt': {control: 58},
    '/kit0/adpars/GlobalPar/FreqEnvelope/PR_dt': {control: 59},
    '/kit0/adpars/GlobalPar/FreqEnvelope/PR_val': {control: 60},
    '/kit0/adpars/GlobalPar/FreqLfo/Pfreq': {control: 61, map: v=>parseInt(127*v), type: 'f', action: ()=>{send('127.0.0.1', zyn_port, `/part${zyn_selected}/kit0/adpars/GlobalPar/FreqLfo/Pstartphase`, {type: 'i', value:0})}},
    '/kit0/adpars/GlobalPar/FreqLfo/Pintensity': {control: 62},
    '/kit0/adpars/GlobalPar/FreqLfo/PLFOtype': {control: 64, map: midiSteps(8)},
    '/kit0/adpars/GlobalPar/FilterEnvelope/PA_dt': {control: 65},
    '/kit0/adpars/GlobalPar/FilterEnvelope/PD_val': {control: 66},
    '/kit0/adpars/GlobalPar/FilterEnvelope/PD_dt': {control: 67},
    '/kit0/adpars/GlobalPar/FilterEnvelope/PR_dt': {control : 68},
    '/kit0/adpars/GlobalPar/FilterLfo/Pfreq': {control: 69, map: v=>parseInt(127*v), type: 'f', forcefeedback: true, action: ()=>{send('127.0.0.1', zyn_port, `/part${zyn_selected}/kit0/adpars/GlobalPar/FilterLfo/Pstartphase`, {type: 'i', value:0})}},
    '/kit0/adpars/GlobalPar/FilterLfo/Pintensity': {control: 70},
    '/kit0/adpars/GlobalPar/FilterLfo/PLFOtype': {control: 72, map: midiSteps(8)},
    '/kit0/adpars/GlobalPar/GlobalFilter/Pcategory': {control: 101, forcefeedback: true},
}

forcedfeedbacks = Object.keys(bcr_mapping).filter(x=>bcr_mapping[x].forcefeedback)


function queryZyn(n) {
    if (debug) send('127.0.0.1', 8645, '/log', `QUERY ZYN`)

    var root = `/part${n}`
    for (var address in bcr_mapping) {
        send('127.0.0.1', zyn_port, root + address)
    }

}

function queryZynAll() {

    statesave = true

    for (var n in bcr_scenes) {
        queryZyn(n)
    }

    setTimeout(()=>{
        statesave = false
    }, 1000)

}

setInterval(()=>{
    for (var address of forcedfeedbacks) {
        send('127.0.0.1', zyn_port, `/part${zyn_selected}${address}`)
        if (debug) send('127.0.0.1', 8645, '/log', `OSC OUT: /part${zyn_selected}${address}`)
    }

}, 250)

module.exports = {

    init: ()=>{

        setTimeout(queryZynAll, 3000)

    },

    oscInFilter: (data)=>{

        var {address, args, host, port} = data
        if (!address.includes('ecasound')) if (debug) send('127.0.0.1', 8645, '/log', `OSC IN: ${JSON.stringify(data)}`)

        if (port === zyn_port) {

            // ignore active keys feedback
            if (address === '/active_keys') return

            // get zyn part number, strip address part prefix
            var [_, part, paramAddress] = address.match(/^\/part([0-9]+)(\/.*)/) || [],
                parameter = bcr_mapping[paramAddress]

            if (statesave) {
                state[parseInt(part)][paramAddress] = args[0].value
            }
            tmpstate[parseInt(part)][paramAddress] = args[0].value

            // copy feedback to bcr if part is selected
            if (parseInt(part) === zyn_selected && parameter) {

                var cc = parameter.control,
                    value = parameter.map ?
                        parameter.map(args[0].value) :
                        args[0].value

                send('midi', midi_port, '/control', 1, cc, value)
                if (debug) send('127.0.0.1', 8645, '/log', `BCR feedback sent: cc ${cc} ${value}`)

                if (parameter.action) {
                    parameter.action(value)
                }


            }
            // if (debug) send('127.0.0.1', 8645, '/log', `ZYN in: ${address} ${args[0].value} (control ${cc} ${value})`)


        }

        else if (port === bcr_port) {

            return

        }

        return {address, args, host, port}

    },

    oscOutFilter: (data)=>{

        var {address, args, host, port} = data

        if (debug) send('127.0.0.1', 8645, '/log', `OSC OUT: ${JSON.stringify(data)}`)


        if (host === 'zyn') {

            if (address === '/select') {

                zyn_selected = args[0].value
                send('127.0.0.1', bcr_port, '/mididings/switch_scene', bcr_scenes[zyn_selected])
                queryZyn(zyn_selected)
                return
            }

            if (address === '/reset') {
                send('127.0.0.1', 8645, '/log', `STATE set: ${JSON.stringify(state)}`)

                var part = args[0].value
                if (!state[part]) return
                var root = `/part${part}`
                for (var address in state[part]) {
                    var val = state[part][address]
                    if (bcr_mapping[address].type !== 'f') val = {type: 'i', value: val}
                    send('127.0.0.1', zyn_port, root + address, val)
                }
                return
            }

            return

        }

        if (address === '/cmescene') {
            address = '/mididings/switch_scene'
        }

        return {address, args, host, port}

    }

}
