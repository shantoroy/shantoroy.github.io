// Certification metadata structure
const certifications = {
    "aws-ai-practitioner": {
        id: "aws-ai-practitioner",
        name: "AWS Certified AI Practitioner (AIF-C01)",
        file: "data/aws-ai-practitioner.json"
    },
    "gcp-associate": {
        id: "gcp-associate",
        name: "Google Cloud Associate Cloud Engineer",
        file: "data/gcp-associate.json"
    },
    "python-cert": {
        id: "python-cert",
        name: "Python Certified Programmer",
        file: "data/python-cert.json"
    }
};

// Cache for loaded question data
const questionCache = {};

// Load questions for a specific certification
async function loadCertificationQuestions(certId) {
    // Return from cache if already loaded
    if (questionCache[certId]) {
        return questionCache[certId];
    }
    
    try {
        // Fetch the questions JSON file
        const response = await fetch(certifications[certId].file);
        if (!response.ok) {
            throw new Error(`Failed to load questions for ${certId}: ${response.status}`);
        }
        
        const questions = await response.json();
        
        // Store in cache
        questionCache[certId] = questions;
        return questions;
    } catch (error) {
        console.error(`Error loading questions for ${certId}:`, error);
        // Instead of returning an empty array, throw the error
        // so it can be handled by the calling function
        throw error;
    }
}