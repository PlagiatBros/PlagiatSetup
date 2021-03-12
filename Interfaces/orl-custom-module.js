var submodules = [
    require('./modules/mididings.js'),
    require('./modules/sooperlooper.js'),
    require('./modules/nonmixer.js'),
    require('./modules/synth.js'),
    require('./modules/lights.js')
]


module.exports = {
    init: function(){

        for (var m of submodules) {
            m.init()
        }

    },
    oscInFilter: function(data){

        for (var m of submodules) {
            data = m.oscInFilter(data)
            if (!data) return
        }

        return data

    },
    oscOutFilter: function(data){

        for (var m of submodules) {
            data = m.oscOutFilter(data)
            if (!data) return
        }

        return data
    }
}
