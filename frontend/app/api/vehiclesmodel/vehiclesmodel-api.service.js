(function(){
    "use strict";

    angular.module('vehiclesmodel-api').factory('VehiclesModelApi', VehiclesModelApi);

    function VehiclesModelApi(Ajax){
        
        var manufactureApiById = 'api/1/vehiclesmodel/<vehiclesmodel-id>/';
        var vehiclesModelEndpoint = 'api/1/vehiclesmodel/';

        var restApi = {
            getVehiclesModel: getVehiclesModel,
            deleteVehiclesModelById: deleteVehiclesModelById,
            saveVehicleModel: saveVehicleModel,
            updateVehicleModel: updateVehicleModel,
        };

        return restApi;

        function getVehiclesModel(){
           return Ajax.get(vehiclesModelEndpoint);
        }

        function deleteVehiclesModelById(id){
            var url = manufactureApiById.replace("<vehiclesmodel-id>", id);
            return Ajax.del(url);
        }

        function saveVehicleModel(params){
            return Ajax.post(vehiclesModelEndpoint, params);
        }

        function updateVehicleModel(params){
            var id = params.vehiclemodel_dict.id;
            var url = manufactureApiById.replace("<vehiclesmodel-id>", id);
            return Ajax.post(url, params);
        }
    }
})();