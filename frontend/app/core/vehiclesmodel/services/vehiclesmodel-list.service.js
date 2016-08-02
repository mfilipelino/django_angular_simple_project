(function(){
	"use strict";

	angular.module('vehiclesmodel').factory('VehiclesModelListService', VehiclesModelListService);


	function VehiclesModelListService(VehiclesModelApi, ManufacturesApi){

		var ctrl = this;

		var service = {
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
			service.motorChoiceCar =  ["125", "250", "500", "1000", "1200", "1400", "1600", "1800", "2000"];

			service.stateVehicleModelEdit = {
				vehicle_type: '',
				name: "",
				manufacture_name: '',
				motor: "",
			};

			_getManufactures();
			return _getVehiclesModel();
			
		}

		function _getVehiclesModel(){

			var promisse = VehiclesModelApi.getVehiclesModel();
			promisse.then(sucess, erro);

			function sucess(result){
				service.vehiclesModel = result.data.vehicles_models;
			}

			function erro(result){
				alert(result.data);
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

			function erro(result){
				alert(result.data);
			}

		}

		function _searchNameManufacture(array, id){
			for( var element in array){
				if(element.id === id){
					return element;
				}
			}
			return {
				name: "",
			};
		}


		function editVehicleModelUpdateView(index){
			var manufacture_id = service.vehiclesModel[index].manufacturer_id;
			var array = service.manufactures;
			service.stateVehicleModelEdit = {
				vehicle_type: service.vehiclesModel[index].vehicle_type,
				name: service.vehiclesModel[index].name,
				motor: "" + service.vehiclesModel[index].motor,
				manufacture_name: _searchNameManufacture(array, manufacture_id).name,
			};
			service.vehiclesModel[index];
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

			var vehiclemodel_params = {
				name: service.stateVehicleModelEdit.name,
				manufacturer_id: service.stateVehicleModelEdit.selectedManufacture.id,
				motor: service.stateVehicleModelEdit.selectedMotor,
				vehicle_type: service.stateVehicleModelEdit.selectedVehicleType, 
			}

			var params = {
				vehiclemodel_dict: vehiclemodel_params,
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
				alert(result.data);
			}
		}

		function saveVehicleModelUpdateView(){

			var promisse = _saveVehicleModel().then(sucess, error);
			service.clearEdit();
			return promisse;

			function sucess(result){
				
			}

			function error(result){
				alert(result.data);
			}

		}

		function clearEdit(){
			console.log("clear");
			service.stateVehicleModelEdit = {};
			service.isCreate = true;
		}
	}

})();