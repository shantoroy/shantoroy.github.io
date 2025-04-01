// Certification metadata structure
const certifications = {
    "aws-ai-practitioner": {
        id: "aws-ai-practitioner",
        name: "AWS Certified AI Practitioner (AIF-C01)",
        file: "data/aws-ai-practitioner.json"
    },
    // "gcp-associate": {
    //     id: "gcp-associate",
    //     name: "Google Cloud Associate Cloud Engineer",
    //     file: "data/gcp-associate.json"
    // },
    "scrum-developer": {
        id: "scrum-developer",
        name: "Professional Scrum Developer I (PSD I)",
        file: "data/scrum-developer.json"
    },
    "scrum-master": {
        id: "scrum-master",
        name: "Professional Scrum Master I (PSM I)",
        file: "data/scrum-master.json"
    },
    "github-actions": {
        id: "github-actions",
        name: "GitHub Actions (GitHub CI/CD)",
        file: "data/github-actions.json"
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