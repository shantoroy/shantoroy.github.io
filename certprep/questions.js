// Certification metadata structure
const certifications = {
    "gcp-associate": {
        id: "gcp-associate",
        name: "Associate Cloud Engineer (GCP ACE)",
        file: "data/gcp-associate.json"
    },
    "aws-solution-architect": {
        id: "aws-solution-architect",
        name: "AWS Solutions Architect (SAA-C03)",
        file: "data/aws-solution-architect.json"
    },
    "aws-ai-practitioner": {
        id: "aws-ai-practitioner",
        name: "AWS AI Practitioner (AIF-C01)",
        file: "data/aws-ai-practitioner.json"
    },
    "aws-cloud-practitioner": {
        id: "aws-cloud-practitioner",
        name: "AWS Cloud Practitioner (CLF-C02)",
        file: "data/aws-cloud-practitioner.json"
    },
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
    },
    "github-foundations": {
        id: "github-foundations",
        name: "GitHub Foundations (GitHub Basic)",
        file: "data/github-foundations.json"
    },
    "github-security": {
        id: "github-security",
        name: "GitHub Advanced Security (GH Security)",
        file: "data/github-security.json"
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