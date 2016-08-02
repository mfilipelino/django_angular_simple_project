(function(){
    "use strict";

    angular.module('vehiclesmodel-api').factory('VehiclesModelApi', VehiclesModelApi);

    function VehiclesModelApi(Ajax){
        
        var manufactureApiById = 'api/1/vehiclesmodel/<vehiclesmodel-id>/';
        var projectsApiBulkEndpoint = 'api/1/vehiclesmodel/';

        var restApi = {
            getVehiclesModel: getVehiclesModel,
            deleteVehiclesModelById: deleteVehiclesModelById,
            saveVehicleModel: saveVehicleModel,
        };

        return restApi;

        function getVehiclesModel(){
           return Ajax.get(projectsApiBulkEndpoint);
        }

        function deleteVehiclesModelById(id){
            var url = manufactureApiById.replace("<vehiclesmodel-id>", id);
            return Ajax.del(url);
        }

        function saveVehicleModel(params){
            return Ajax.post(projectsApiBulkEndpoint, params);
        }
    }
})();