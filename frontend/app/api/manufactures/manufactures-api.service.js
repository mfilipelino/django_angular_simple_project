(function(){
    "use strict";

    angular.module('manufactures-api').factory('ManufacturesApi', ManufacturesApi);

    function ManufacturesApi(Ajax){
        
        var manufactureApiById = 'api/1/manufactures/<manufactures-id>/';
        var projectsApiBulkEndpoint = 'api/1/manufactures/';

        var restApi = {
            getManufactures: getManufactures,
            deleteManufactureById: deleteManufactureById,
        };

        return restApi;

        function getManufactures(){
           return Ajax.get(projectsApiBulkEndpoint);
        }

        function deleteManufactureById(id){
            var url = manufactureApiById.replace("<manufactures-id>", id);
            return Ajax.del(url);
        }

    }
})();