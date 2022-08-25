// SPDX-License-Identifier: MIT
pragma solidity >=0.5.16;

contract eVOT_Contract
{
	struct Candidat
	{
		uint id;
		string nume;
		uint nr_voturi;
	}

	mapping(address => bool) private listaVoturi;
	mapping(uint => Candidat) private candidat;

	uint private nr_Candidat;

    modifier DoarDacaNuAmVotat
	{
        require(listaVoturi[msg.sender] == false, "Ai votat deja!");
		// you can use throw instead;
        _;
    }

	function adaugaCandidat(string memory _nume) public
	{
		nr_Candidat++;
		candidat[nr_Candidat] = Candidat(nr_Candidat, _nume, 0);
	}

	function voteaza(uint _candidatID) public DoarDacaNuAmVotat
	{
        // Checking the candidate is a valid
        require(
        	_candidatID > 0 && _candidatID <= nr_Candidat
        	//"Invalid candidate"
        );

		// update candidate vote count
		candidat[_candidatID].nr_voturi++;
		listaVoturi[msg.sender] = true;
	}

	function Info_Candidat(uint _id) public view returns(string memory, uint)
	{
		return (candidat[_id].nume, candidat[_id].nr_voturi);
	}

	function getRezultate(uint _candidatID) public view returns(uint)
	{
		return (candidat[_candidatID].nr_voturi);
	}

	function sender() public view returns(address)
	{
		return (msg.sender);
	}

	function getNume(uint _candidatID) public view returns(string memory )
	{
		return candidat[_candidatID].nume;
	}

	function resetCandidat() public
	{
		for (uint i = 1; i <= nr_Candidat; i++)
		{
			delete candidat[i];
		}
		nr_Candidat = 0;
	}
}