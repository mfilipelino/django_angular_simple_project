(function(){
    "use strict";

    angular.module('vehicles-api').factory('VehiclesApi', VehiclesApi);

    function VehiclesApi(Ajax){
        
        var manufactureApiById = 'api/1/vehicles/<vehicles-id>/';
        var vehiclesApiEndPoint = 'api/1/vehicles/';

        var restApi = {
            getVehicles: getVehicles,
            deleteVehiclesById: deleteVehiclesById,
            saveManufacture: saveManufacture,
        };

        return restApi;

        function getVehicles(){
           return Ajax.get(vehiclesApiEndPoint);
        }

            function deleteVehiclesById(id){
                var url = manufactureApiById.replace("<vehicles-id>", id);
                return Ajax.del(url);
            }

        function saveManufacture(params){
            return Ajax.post(vehiclesApiEndPoint, params);
        }
    }
})();