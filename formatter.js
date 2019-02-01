module.exports = function(proofJson) {
    let p = proofJson;
    let all = [p.proof.A, p.proof.A_p, p.proof.B, p.proof.B_p, p.proof.C, p.proof.C_p, p.proof.H, p.proof.K, p.input];
    // return JSON.stringify(all).slice(1,-1);
    return all;
}
