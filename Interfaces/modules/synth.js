zyn_port = 9090
bcr_port = 12345
zyn_selected = 0

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
    '/kit0/partefx1/EQ/filter0/Pfreq': {control: 8},
    '/kit0/adpars/GlobalPar/GlobalFilter/Ptype': {control: 33},
    '/kit0/adpars/GlobalPar/octave': {control: 41, map: v=>v+2},
    '/kit0/adpars/GlobalPar/AmpEnvelope/PA_dt': {control: 49},
    '/kit0/adpars/GlobalPar/AmpEnvelope/PD_dt': {control: 50},
    '/kit0/adpars/GlobalPar/AmpEnvelope/PS_val': {control: 51},
    '/kit0/adpars/GlobalPar/AmpEnvelope/PR_dt': {control: 52},
    '/kit0/adpars/GlobalPar/AmpLfo/Pfreq': {control: 53},
    '/kit0/adpars/GlobalPar/AmpLfo/Pintensity': {control: 54},
    '/kit0/adpars/GlobalPar/AmpLfo/PLFOtype': {control: 56, map: midiSteps(8)},
    '/kit0/adpars/GlobalPar/FreqEnvelope/PA_val': {control: 57},
    '/kit0/adpars/GlobalPar/FreqEnvelope/PA_dt': {control: 58},
    '/kit0/adpars/GlobalPar/FreqEnvelope/PR_dt': {control: 59},
    '/kit0/adpars/GlobalPar/FreqEnvelope/PR_val': {control: 60},
    '/kit0/adpars/GlobalPar/FreqLfo/Pfreq': {control: 61, map: v=>parseInt(127*v)},
    '/kit0/adpars/GlobalPar/FreqLfo/Pintensity': {control: 62},
    '/kit0/adpars/GlobalPar/FreqLfo/PLFOtype': {control: 64, map: midiSteps(8)},
    '/kit0/adpars/GlobalPar/FilterEnvelope/PA_dt': {control: 65},
    '/kit0/adpars/GlobalPar/FilterEnvelope/PD_val': {control: 66},
    '/kit0/adpars/GlobalPar/FilterEnvelope/PD_dt': {control: 67},
    '/kit0/adpars/GlobalPar/FilterEnvelope/PR_dt': {control: 68},
    '/kit0/adpars/GlobalPar/FilterLfo/Pfreq': {control: 69},
    '/kit0/adpars/GlobalPar/FilterLfo/Pintensity': {control: 70},
    '/kit0/adpars/GlobalPar/FilterLfo/PLFOtype': {control: 72, map: midiSteps(8)},
    '/kit0/adpars/GlobalPar/GlobalFilter/Pcategory': {control: 101, action: v=>send('127.0.0.1', bcr_port, '/mididings/switch_subscene', v === 1 ? 2 : 1)},
}

function queryZyn(n) {

    var root = `/part${n}`
    for (var address in bcr_mapping) {
        send('127.0.0.1', zyn_port, root + address)
    }

}

function queryZynAll() {

    for (var n = 0; i < 6; i++) {
        queryZyn(i)
    }

}


module.exports = {

    init: ()=>{

        setTimeout(queryZynAll, 5000)

    },

    oscInFilter: (data)=>{

        var {address, args, host, port} = data

        if (port === zyn_port) {

            // ignore active keys feedback
            if (address === '/active_keys') return

            // get zyn part number, strip address part prefix
            var [_, part, paramAddress] = address.match(/^\/part([0-9]+)(\/.*)/) || [],
                parameter = bcr_mapping[paramAddress]

            // copy feedback to bcr if part is selected
            if (parseInt(part) === zyn_selected && parameter) {

                var cc = bcr_mapping[parameter].control,
                    value = bcr_mapping[parameter].map ?
                        bcr_mapping[parameter].map(args[0].value) :
                        args[0].value

                send('midi', 'bcr_feedback', '/control', cc, value)

                if (bcr_mapping[parameter].action) {
                    bcr_mapping[parameter].action(value)
                }

            }

        }

        else if (port === bcr_port) {

            return

        }

        return {address, args, host, port}

    },

    oscOutFilter: (data)=>{

        var {address, args, host, port} = data


        if (host === 'zyn') {

            if (address === '/select') {

                zyn_selected = args[0].value
                queryZyn(zyn_selected)
                return
            }

        }

        if (address === '/cmescene') {
            address = '/mididings/switch_scene'
        }

        return {address, args, host, port}

    }

}
