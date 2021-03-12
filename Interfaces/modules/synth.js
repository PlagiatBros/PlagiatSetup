zyn_port = 9090
bcr_port = 12345
zyn_selected = 0

function midiSteps(steps) {
    return (v)=>{
        return parseInt(127*v/steps)
    }
}

bcr_mapping = {
    'GlobalFilter/Pfreq': {control: 1},
    'GlobalFilter/Pcenterfreq': {control: 1},
    'GlobalFilter/Pnumformants': {control: 4, map: midiSteps(12)},
    'GlobalFilter/Poctavesfreq': {control: 5},
    'GlobalFilter/Pq': {control: 2},
    'GlobalFilter/Pstages': {control: 3, map: midiSteps(5)},
    'PBandwidth': {control: 6},
    'PCoarseDetune': {control: 7},
    'partefx1/EQ/filter0/Pfreq': {control: 8},
    'GlobalFilter/Ptype': {control: 33},
    'octave': {control: 41, map: v=>v+2},
    'AmpEnvelope/PA_dt': {control: 49},
    'AmpEnvelope/PD_dt': {control: 50},
    'AmpEnvelope/PS_val': {control: 51},
    'AmpEnvelope/PR_dt': {control: 52},
    'AmpLfo/Pfreq': {control: 53},
    'AmpLfo/Pintensity': {control: 54},
    'AmpLfo/PLFOtype': {control: 56, map: midiSteps(8)},
    'FreqEnvelope/PA_val': {control: 57},
    'FreqEnvelope/PA_dt': {control: 58},
    'FreqEnvelope/PR_dt': {control: 59},
    'FreqEnvelope/PR_val': {control: 60},
    'FreqLfo/Pfreq': {control: 61, map: v=>parseInt(127*v)},
    'FreqLfo/Pintensity': {control: 62},
    'FreqLfo/PLFOtype': {control: 64, map: midiSteps(8)},
    'FilterEnvelope/PA_dt': {control: 65},
    'FilterEnvelope/PD_val': {control: 66},
    'FilterEnvelope/PD_dt': {control: 67},
    'FilterEnvelope/PR_dt': {control: 68},
    'FilterLfo/Pfreq': {control: 69},
    'FilterLfo/Pintensity': {control: 70},
    'FilterLfo/PLFOtype': {control: 72, map: midiSteps(8)},
    'GlobalFilter/Pcategory': {control: 101},
}

bcr_address_cache = {}

function queryZyn(n) {

    var root1 = `/part${n}/kit0/`,
        root2 = 'adpars/GlobalPar/'
    for (var k in bcr_mapping) {
        var address = k === 'partefx1/EQ/filter0/Pfreq' ?
            root1 + k : root1 + root2 + k

        send('127.0.0.1', zyn_port, address)

    }

}

function queryZynAll() {

    for (var n = 0; i < 6; i++) {
        queryZyn(i)
    }

}


module.exports = {

    init: ()=>{


    },

    oscInFilter: (data)=>{

        var {address, args, host, port} = data

        if (port === zyn_port) {

            // ignore active keys feedback
            if (address === '/active_keys') return


            // check address against bcr mapping
            var parameter = bcr_address_cache[address]
            if (!parameter) {
                for (var k in bcr_mapping) {
                    if (address.endsWith(k)) {
                        parameter = k
                        bcr_address_cache[address] = k
                        break
                    }
                }
            }

            // copy feedback to bcr
            if (parameter) {

                var cc = bcr_mapping[parameter],
                    value = bcr_mapping[parameter].map ?
                        bcr_mapping[parameter].map(args[0].value) :
                        args[0].value

                send('midi', 'bcr_feedback', '/control', cc, value)

                if (parameter === 'GlobalFilter/Pcategory') {
                    send('127.0.0.1', bcr_port, '/mididings/switch_subscene', value === 1 ? 2 : 1)
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
