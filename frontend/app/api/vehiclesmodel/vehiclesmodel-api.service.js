(function(){
    "use strict";

    angular.module('manufactures-api').factory('VehiclesModelApi', VehiclesModelApi);

    function VehiclesModelApi(Ajax){
        
        var manufactureApiById = 'api/1/vehiclesmodel/<vehiclesmodel-id>/';
        var projectsApiBulkEndpoint = 'api/1/vehiclesmodel/';

        var restApi = {
            getManufactures: getManufactures,
            deleteManufactureById: deleteManufactureById,
            saveManufacture: saveManufacture,
        };

        return restApi;

        function getManufactures(){
           return Ajax.get(projectsApiBulkEndpoint);
        }

        function deleteManufactureById(id){
            var url = manufactureApiById.replace("<vehiclesmodel-id>", id);
            return Ajax.del(url);
        }

        function saveManufacture(params){
            return Ajax.post(projectsApiBulkEndpoint, params);
        }
    }
})();