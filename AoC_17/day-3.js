// Day 2

// Part 1
console.log("Part 1");

console.log(getManhattanDistance(312051));

function getManhattanDistance (n) {
	var seqIdx = 0;
	while (seqCalc(seqIdx, -3) < n) {
		seqIdx++;
	}
	if (seqCalc(seqIdx, -3) === n) { 
		return seqIdx;
	}
	seqIdx--;

	var seqNum = -2;
	var seqVal = seqCalc(seqIdx, seqNum);
	while (seqVal < n && seqNum < 5) {
		seqNum++;
		seqVal = seqCalc(seqIdx, seqNum);
	}
	if (seqNum !== 5 && seqCalc(seqIdx, seqNum) === n) {
		return seqIdx * (seqNum % 2 === 0 ? 2 : 1);
	}
	seqNum--;

	var offset = 0;
	var val = seqCalc(seqIdx, seqNum);
	while (val < n) {
		val++;
		offset++;
	}


	if (seqNum % 2 !== 0) {
		return seqIdx + offset;
	} else if (seqNum !== 4) {
		return (2 * seqIdx) - offset;
		// if 4 then + 1 offset
	} else {
		return (2 * seqIdx) - (offset - 1) + 1;
	}

}

function seqCalc (i, nMod) {
	return (4 * i * i) + (nMod * i) + 1;
}


// Part 2
console.log("Part 2");

function fuckingPieceOfShit (n) {
	var currVal = 1;

	while (currVal <= n) {
		
	}
}