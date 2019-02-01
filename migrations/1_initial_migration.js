let Migrations = artifacts.require("Migrations.sol");
let Verifier = artifacts.require("Verifier.sol");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(Verifier);
};
