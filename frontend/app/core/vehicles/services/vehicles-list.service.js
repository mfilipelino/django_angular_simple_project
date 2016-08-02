(function(){
	"use strict";

	angular.module('vehicles').factory('VehiclesListService', VehiclesListService);


	function VehiclesListService(VehiclesApi){

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
			var promisse = VehiclesApi.getManufactures();
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
			var promisse = VehiclesApi.deleteManufactureById(id)
								.then(function(result){
									service.manufactures.splice(index, 1);
							});
			return promisse;
		}

		function _saveManufacture(){
			var params = {
				manufacture_dict: service.stateManufactureEdit,
			};
			var promisse = VehiclesApi.saveManufacture(params);
			return promisse;
		}

		function saveManufacturePushView(){

			var promisse = _saveManufacture().then(sucess).then(error);
			return promisse;

			function sucess(result){
				service.manufactures.push(result.data);
			}

			function error(result){
				BootstrapDialog.alert('I want banana!');
			}
		}

		function saveManufactureUpdateView(){

			var promisse = _saveManufacture().then(sucess(result)).then(error(result));
			service.clearEdit();
			return promisse;

			function sucess(result){
				console.log("sucess");
			}

			function error(result){
				BootstrapDialog.alert('I want banana!');
			}

		}

		function clearEdit(){
			console.log("clear");
			service.stateManufactureEdit = {};
			service.isCreate = true;
		}
	}

})();