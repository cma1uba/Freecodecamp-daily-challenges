/**
 * Given two strings (fingerprintA and fingerprintB) representing fingerprints,
 * determines if they are a match based on length and difference count (<= 10%).
 * * @param {string} fingerprintA - The first fingerprint string.
 * @param {string} fingerprintB - The second fingerprint string.
 * @returns {boolean} True if the fingerprints match, otherwise False.
 */
 
function isMatch(fingerprintA, fingerprintB) {
    // 1. Check for the same length
    if (fingerprintA.length !== fingerprintB.length) {
        return false;
    }

    const length = fingerprintA.length;
    
    // Handle the edge case of empty strings
    if (length === 0) {
        return true;
    }

    // 2. Calculate the maximum allowed difference
    // Math.floor ensures to get an integer
    const maxDiffAllowed = Math.floor(length * 0.10); 
    
    // 3. Count the differing characters
    let diffCount = 0;
    
    for (let i = 0; i < length; i++) {
        if (fingerprintA[i] !== fingerprintB[i]) {
            diffCount++;
            
            // Optimization: If the difference count exceeds the maximum allowed, stop early.
            if (diffCount > maxDiffAllowed) {
                return false;
            }
        }
    }
    
    // If the loop completes, it means the diffCount was within the allowed limit.
    return true;
}
