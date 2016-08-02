(function(){
	"use strict";

	angular.module('manufactures').factory('ManufacturesListService', ManufacturesListService);


	function ManufacturesListService(ManufacturesApi){

		var service = {
			stateManufactureEdit: {
				name:""
			},
			init: init,
			editManufactureUpdateView: editManufactureUpdateView,
			deleleteManufacturePopView: deleleteManufacturePopView,
			saveManufacturePushView: saveManufacturePushView,
			saveManufactureUpdateView: saveManufactureUpdateView,
			clearEdit: clearEdit,

		};
		return service;

		function init(){
			service.manufactures = [];
			service.isCreate = true;
			var promisse = ManufacturesApi.getManufactures();
			promisse.then(function(result){
				service.manufactures = result.data.manufactures;
			});
			return promisse;
		}


		function editManufactureUpdateView(index){
			service.stateManufactureEdit = service.manufactures[index];
			service.isCreate = false;
		}

		function deleleteManufacturePopView(index){
			var id = service.manufactures[index].id;
			var promisse = ManufacturesApi.deleteManufactureById(id)
								.then(function(result){
									service.manufactures.splice(index, 1);
							});
			return promisse;
		}

		function _saveManufacture(){
			var params = {
				manufacture_dict: service.stateManufactureEdit,
			};
			var promisse = ManufacturesApi.saveManufacture(params);
			return promisse;
		}



		function saveManufacturePushView(){

			if( _validationManufacture() ){
				return {};
			}

			var promisse = _saveManufacture().then(sucess, error);
			return promisse;

			function sucess(result){
				service.manufactures.push(result.data);
			}

			function error(result){
				alert(result.data);
			}
		}

		function saveManufactureUpdateView(){

			if(_validationManufacture() ){
				return {};
			}

			var promisse = _saveManufacture().then(sucess, error);
			service.clearEdit();
			return promisse;

			function sucess(result){
				console.log("sucess");
			}

			function error(result){
				alert(error.data);
			}

		}

		function clearEdit(){
			console.log("clear");
			service.stateManufactureEdit = {};
			service.isCreate = true;
		}

		function _validationManufacture(){
			return service.stateManufactureEdit.name == "";
		}
	}

})();