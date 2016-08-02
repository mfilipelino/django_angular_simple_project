(function(){
	"use strict";

	angular.module('manufactures').factory('VehiclesModelListService', VehiclesModelListService);


	function VehiclesModelListService(VehiclesModelApi, ManufacturesApi){

		var service = {
			stateVehicleModelEdit: {
				vehicle_type: 'car',
				name: "",
				manufacturer_id: 1,
				motor: 0,
			},
			init: init,
			editVehicleModelUpdateView: editVehicleModelUpdateView,
			deleteVehicleModelPopView: deleteVehicleModelPopView,
			saveVehicleModelPushView: saveVehicleModelPushView,
			saveVehicleModelUpdateView: saveVehicleModelUpdateView,
			clearEdit: clearEdit,

		};
		return service;

		function init(){
			service.vehiclesModel = [];
			service.isCreate = true;
			service.selectManufacture = {};
			service.vehicleTypeChoice = ['car', 'bike'];
			service.motorChoiceCar =  [1000, 1200, 1400, 1600, 1800, 2000]; 
			service.motorChoiceBike = [125, 250, 500, 1000 ];
			_getManufactures();

			var promisse = VehiclesModelApi.getVehiclesModel();
			promisse.then(sucess, erro);

			function sucess(result){
				service.vehiclesModel = result.data.vehicles_models;
			}

			function erro(result){
				alert(error.data);
			}
			return promisse;
		}

		function _getManufactures(){
			var promisse = ManufacturesApi.getManufactures();
			promisse.then(sucess, erro);
			return promisse;

			function sucess(result){
				service.manufactures = result.data.manufactures;
			}

			function erro(){
				console.log(result.data);
			}
		}


		function editVehicleModelUpdateView(index){
			service.stateManufactureEdit = service.manufactures[index];
			service.isCreate = false;
		}

		function deleteVehicleModelPopView(index){
			var id = service.vehiclesModel[index].id;
			var promisse = VehiclesModelApi.deleteVehiclesModelById(id)
								.then(function(result){
									service.vehiclesModel.splice(index, 1);
							});
			return promisse;
		}

		function _saveVehicleModel(){
			var params = {
				vehiclemodel_dict: service.stateVehicleModelEdit,
			};
			var promisse = VehiclesModelApi.saveVehicleModel(params);
			return promisse;
		}

		function saveVehicleModelPushView(){

			var promisse = _saveVehicleModel().then(sucess, error);
			return promisse;

			function sucess(result){
				service.vehiclesModel.push(result.data);
			}

			function error(result){
				alert(error.data);
			}
		}

		function saveVehicleModelUpdateView(){

			var promisse = _saveVehicleModel().then(sucess, error);
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
	}

})();