(function(){
    "use strict";

    angular.module('vehicles-api').factory('VehiclesApi', VehiclesApi);

    function VehiclesApi(Ajax){
        
        var manufactureApiById = 'api/1/manufactures/<manufactures-id>/';
        var projectsApiBulkEndpoint = 'api/1/manufactures/';

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
            var url = manufactureApiById.replace("<manufactures-id>", id);
            return Ajax.del(url);
        }

        function saveManufacture(params){
            return Ajax.post(projectsApiBulkEndpoint, params);
        }
    }
})();