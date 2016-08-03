(function(){
    "use strict";

    angular.module('vehicles-api').factory('VehiclesApi', VehiclesApi);

    function VehiclesApi(Ajax){
        
        var manufactureApiById = 'api/1/vehicles/<vehicles-id>/';
        var vehiclesApiEndPoint = 'api/1/vehicles/';

        var restApi = {
            getVehicles: getVehicles,
            deleteVehiclesById: deleteVehiclesById,
            saveVehicle: saveVehicle,
            updateVehicle: updateVehicle,
        };

        return restApi;

        function getVehicles(){
           return Ajax.get(vehiclesApiEndPoint);
        }

        function deleteVehiclesById(id){
            var url = manufactureApiById.replace("<vehicles-id>", id);
            return Ajax.del(url);
        }

        function saveVehicle(params){
            return Ajax.post(vehiclesApiEndPoint, params);
        }

         function updateVehicle(params){
            var id = params.vehicle_dict.id;
            var url = manufactureApiById.replace("<vehicles-id>", id);
            return Ajax.post(url, params);
        }
    }
})();