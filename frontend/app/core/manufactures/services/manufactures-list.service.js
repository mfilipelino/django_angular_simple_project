(function(){
	"use strict";

	angular.module('manufactures').factory('ManufacturesListService', ManufacturesListService);


	function ManufacturesListService(ManufacturesApi){
		var service = {
			init: init,
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
	}

})();