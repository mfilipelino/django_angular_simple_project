(function(){
    'use strict';
    
    if (!window.GLOBAL) {
        window.GLOBAL = {};
    }

    GLOBAL.isEqualSensitive = function (value1, value2, is_case_sensitive) {
        if (is_case_sensitive) {
            return value1 == value2;
        }
        else {
            return value1.toLowerCase() == value2.toLowerCase();
        }
    };

    GLOBAL.indexOfByProperty = function (array, prop, value, is_case_sensitive) {
        is_case_sensitive = typeof is_case_sensitive === "undefined" ? true : is_case_sensitive;
        for (var i = 0; i < array.length; i++) {
            var e = array[i];
            if (GLOBAL.isEqualSensitive(e[prop], value, is_case_sensitive)) {
                return i;
            }
        }
        return -1;
    };

    GLOBAL.getElementByProperty = function (array, prop, value, is_case_sensitive) {
        var elementIndex = GLOBAL.indexOfByProperty(array, prop, value, is_case_sensitive);
        if (elementIndex > -1) {
            return array[elementIndex];
        }
        return null;
    }; 

    GLOBAL.getYearArrayRange = function (start, end) {
        var years = [];
        for(var i = start; i < end; i++){
            years.push(i);
        }
        return years;
    }; 

})();