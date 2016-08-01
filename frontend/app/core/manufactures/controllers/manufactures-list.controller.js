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

		ctrl.save = function(){
			console.log("Create");
			var params = {
				manufacture_dict: ctrl.newManufacture,
			};
			ctrl.service.saveManufacture(params)
				.then(function(){
					console.log("save");
					ctrl.newManufacture = {};
				});
		}
	}

})();


