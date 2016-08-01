(function(){
	'use strict';

	angular.module('manufactures').controller("ManufacturesListController", ManufacturesListController);

	function ManufacturesListController(ManufacturesListService){
		
		var ctrl = this;
		ctrl.service = ManufacturesListService;
		ctrl.service.init();

		ctrl.edit = function(index){
			console.log("Edit indice: " + index + " id: " + ctrl.service.manufactures[index].id + " name: " + ctrl.service.manufactures[index].name);
		};

		ctrl.delete = function(index){
			console.log("Delete indice: " + index + " id: " + ctrl.service.manufactures[index].id + " name: " + ctrl.service.manufactures[index].name);
			ctrl.service.deleteManufactureById(ctrl.service.manufactures[index].id)
				.then(function(result){
					ctrl.service.manufactures.splice(index, 1);
				});
		};

	}

})();