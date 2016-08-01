(function(){
    "use strict";

    angular.module('manufactures-api').factory('ManufacturesApi', ManufacturesApi);

    function ManufacturesApi(Ajax){
        
        var manufactureApiById = 'api/1/manufactures/<manufactures-id>/';
        var projectsApiBulkEndpoint = 'api/1/manufactures/';

        var restApi = {
            getManufactures: getManufactures,
        };

        return restApi;

        function getManufactures(){
           return Ajax.get(projectsApiBulkEndpoint);
        }
                
    }
})();