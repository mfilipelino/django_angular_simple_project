(function(){
	"use strict";

	angular.module('manufactures').factory('ManufacturesListService', ManufacturesListService);


	function ManufacturesListService(ManufacturesApi){
		var service = {
			init: init,
			deleteManufactureById: deleteManufactureById,
			saveManufacture: saveManufacture,
		};
		return service;

		function init(){
			service.manufactures = [];
			var promisse = ManufacturesApi.getManufactures();
			promisse.then(function(result){
				service.manufactures = result.data.manufactures;
			});
			return promisse;
		}

		function deleteManufactureById(id){
			var promisse = ManufacturesApi.deleteManufactureById(id);
			return promisse;
		}

		function saveManufacture(manufacture){
			var promisse = ManufacturesApi.saveManufacture(manufacture);
			return promisse;
		}
	}

})();