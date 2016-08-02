(function(){
	"use strict";

	angular.module('vehiclesmodel').factory('VehiclesModelListService', VehiclesModelListService);


	function VehiclesModelListService(VehiclesModelApi, ManufacturesApi){

		var ctrl = this;

		var service = {
			init: init,
			editVehicleModelUpdateView: editVehicleModelUpdateView,
			deleteVehicleModelPopView: deleteVehicleModelPopView,
			createVehicleModel: createVehicleModel,
			updateVehicleModel: updateVehicleModel,
			clearEdit: clearEdit,
			clearSearch: clearSearch,
			changeManufacturerFilter: changeManufacturerFilter
		};
		return service;

		function init(){

			service.vehiclesModel = [];
			service.isCreate = true;
			service.selectManufacture = {};
			service.vehicleTypeChoice = ['car', 'bike'];
			service.motorChoiceCar =  ["125", "250", "500", "1000", "1200", "1400", "1600", "1800", "2000"];
			service.search = {};

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

		function editVehicleModelUpdateView(index){
			
			var vm = service.vehiclesModel[index];

			var manufacture = GLOBAL.getElementByProperty(service.manufactures, 'id', vm.manufacturer_id);

			service.stateVehicleModelEdit = {
				id: vm.id,
				selectedVehicleType: vm.vehicle_type,
				name: vm.name,
				selectedMotor: vm.motor.toString(),
				selectedManufacture: manufacture,

			};
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
				id: service.stateVehicleModelEdit.id,
				name: service.stateVehicleModelEdit.name,
				manufacturer_id: service.stateVehicleModelEdit.selectedManufacture.id,
				motor: service.stateVehicleModelEdit.selectedMotor,
				vehicle_type: service.stateVehicleModelEdit.selectedVehicleType, 
			};

			var params = {
				vehiclemodel_dict: vehiclemodel_params,
			};

			var promisse;

			if(vehiclemodel_params.id){
				promisse = VehiclesModelApi.updateVehicleModel(params);
			}
			else{
				promisse = VehiclesModelApi.saveVehicleModel(params);
			}
			return promisse;
		}

		function createVehicleModel(){

			var promisse = _saveVehicleModel().then(sucess, error);
			return promisse;

			function sucess(result){
				service.vehiclesModel.push(result.data);
			}

			function error(result){
				alert(result.data);
			}
		}

		function updateVehicleModel(){

			var promisse = _saveVehicleModel().then(sucess, error);
			service.clearEdit();
			return promisse;

			function sucess(result){
				var data = result.data;
				var vehicleModel = GLOBAL.getElementByProperty(service.vehiclesModel, 'id', data.id);
				Object.assign(vehicleModel, data);
			}


			function error(result){
				alert(result.data);
			}

		}

		function clearEdit(){
			service.stateVehicleModelEdit = {};
			service.isCreate = true;
		}

		function clearSearch(){
			service.search = {};
		}

		function changeManufacturerFilter(){
			service.search.manufacturer_id = service.manufacturerFilter.id;
		}
	}

})();