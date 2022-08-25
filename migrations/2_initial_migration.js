const eVot_migrations = artifacts.require("eVOT_Contract");

module.exports = function (deployer) {
  deployer.deploy(eVot_migrations);
};