from flask import Flask, jsonify, render_template

app = Flask(__name__)

missions = {
    # Mars Missions

    "Mangalyaan (Mars Orbiter Mission)": {
        "agency": "ISRO",
        "launch_date": "November 5, 2013",
        "mission_type": "Orbiter",
        "status": "Completed",
        "objectives": "Demonstrate interplanetary mission capability and perform scientific observations of Mars' surface, morphology, and atmosphere",
        "current_location": "Mars orbit (as of mission duration)",
        "key_achievements": [
            "First interplanetary mission by ISRO",
            "First Asian mission to reach Martian orbit",
            "Achieved Mars orbit on the first attempt",
            "Cost-effective mission with a budget of $74 million",
            "Collected data on Martian atmosphere, surface, and mineralogy"
        ]
    },

    
    "Curiosity Rover": {
        "agency": "NASA",
        "launch_date": "November 26, 2011",
        "mission_type": "Rover",
        "status": "Active",
        "objectives": "Investigate Martian climate and geology, assess whether Mars had environmental conditions favorable for microbial life.",
        "current_location": "Mars",
        "key_achievements": [
            "Found evidence of ancient lake beds",
            "Detected organic molecules in rocks",
            "Measured radiation levels for future human missions",
            "Discovered methane variations in atmosphere"
        ]
    },
    
    "Sojourner (Mars Pathfinder)": {
        "agency": "NASA",
        "launch_date": "December 4, 1996",
        "mission_type": "Rover",
        "status": "Completed",
        "objectives": "Demonstrate the feasibility of low-cost landings on and exploration of the Martian surface",
        "current_location": "Mars surface (Ares Vallis region)",
        "key_achievements": [
            "First successful Mars rover operation",
            "Analyzed chemical composition of rocks and soil",
            "Proved micro-rover technology viable on Mars",
            "Operated for 83 days, exceeding 7-day design life",
            "Traveled approximately 100 meters total"
        ]
    },
    
    "Spirit (MER-A)": {
        "agency": "NASA",
        "launch_date": "June 10, 2003",
        "mission_type": "Rover",
        "status": "Completed",
        "objectives": "Study Martian geology and climate history, search for evidence of past water activity",
        "current_location": "Mars surface (Gusev Crater)",
        "key_achievements": [
            "Found evidence of past hydrothermal activity",
            "Discovered silica deposits indicating past water presence",
            "Survived 20x its planned 90-day mission",
            "Traveled 7.73 kilometers",
            "Operated for 2208 sols (Mars days)",
            "Captured over 128,000 images"
        ]
    },
    "Opportunity (MER-B)": {
        "agency": "NASA",
        "launch_date": "July 7, 2003",
        "mission_type": "Rover",
        "status": "Completed",
        "objectives": "Study Martian geology and climate history, search for evidence of past water activity",
        "current_location": "Mars surface (Perseverance Valley)",
        "key_achievements": [
            "Set record for longest distance driven on another planet (45.16 kilometers)",
            "Found evidence of ancient water environments",
            "Discovered first meteorite on another planet",
            "Operated for 14 years (5352 sols)",
            "Survived global dust storm in 2007",
            "Discovered hematite spherules ('blueberries')",
            "Captured over 217,000 images"
        ]
    },
    "Perseverance Rover": {
        "agency": "NASA",
        "launch_date": "July 30, 2020",
        "mission_type": "Rover",
        "status": "Active",
        "objectives": "Search for signs of ancient life, collect samples for possible return to Earth, study Mars' geology and climate.",
        "current_location": "Mars",
        "key_achievements": [
            "First successful Mars helicopter deployment (Ingenuity)",
            "Collection of multiple rock samples for future return",
            "Production of oxygen from Martian atmosphere",
            "Detection of organic molecules in Jezero crater"
        ]
    },
    "Viking 1": {
        "agency": "NASA",
        "launch_date": "August 20, 1975",
        "mission_type": "Orbiter/Lander",
        "status": "Completed",
        "objectives": "First spacecraft to successfully land on Mars and perform long-term science operations",
        "current_location": "Mars surface (inactive)",
        "key_achievements": [
            "First successful Mars landing",
            "First detailed images of Mars surface",
            "First soil analysis on Mars",
            "Operated for 2307 days on Mars surface"
        ]
    },
    "Ingenuity": {
        "agency": "NASA (JPL)",
        "launch_date": "July 30, 2020",
        "mission_type": "Helicopter",
        "status": "Completed",
        "objectives": "Demonstrate the feasibility of powered, controlled flight on another planet",
        "current_location": "Airfield Chi (χ) in Jezero Crater on Mars",
        "key_achievements": [
            "First powered, controlled flight on another planet",
            "Successfully completed multiple flights in the thin Martian atmosphere",
            "Collected aerial imagery and data to support Perseverance rover operations",
            "Pushed the boundaries of rotorcraft flight in extreme environments"
            ]
        },

    # Venus Missions
    "Magellan": {
        "agency": "NASA",
        "launch_date": "May 4, 1989",
        "mission_type": "Orbiter",
        "status": "Completed",
        "objectives": "Map the surface of Venus using radar",
        "current_location": "Destroyed in Venus atmosphere (1994)",
        "key_achievements": [
            "Mapped 98% of Venus surface with radar",
            "Revealed evidence of volcanic activity",
            "Provided detailed topographic data of Venus"
        ]
    },
    
    # Solar System Exploration
    "Voyager 1": {
        "agency": "NASA",
        "launch_date": "September 5, 1977",
        "mission_type": "Interplanetary Probe",
        "status": "Active",
        "objectives": "Study outer space and the outer solar system.",
        "current_location": "Interstellar space",
        "key_achievements": [
            "First spacecraft to enter interstellar space",
            "Closest approach to Jupiter and Saturn",
            "Discovered new moons around Jupiter and Saturn",
            "Captured famous 'Pale Blue Dot' image of Earth"
        ]
    },
    
    # Jupiter Missions
    "Juno": {
        "agency": "NASA",
        "launch_date": "August 5, 2011",
        "mission_type": "Orbiter",
        "status": "Active",
        "objectives": "Study Jupiter's atmosphere, magnetosphere, and gravitational field.",
        "current_location": "Jupiter orbit",
        "key_achievements": [
            "First spacecraft to orbit Jupiter's poles",
            "Revealed Jupiter's internal structure",
            "Discovered cyclones at Jupiter's poles",
            "Provided detailed data about Jupiter's magnetic field"
        ]
    },
    
    # Space Telescopes
    "Hubble Space Telescope": {
        "agency": "NASA/ESA",
        "launch_date": "April 24, 1990",
        "mission_type": "Space Observatory",
        "status": "Active",
        "objectives": "Observe distant galaxies, stars, and nebulae, providing insight into the origins of the universe.",
        "current_location": "Low Earth orbit",
        "key_achievements": [
            "Helped determine age of universe",
            "Discovered dark energy",
            "Observed galaxy formation in early universe",
            "Captured iconic images of deep space objects"
        ]
    },
    "James Webb Space Telescope": {
        "agency": "NASA/ESA/CSA",
        "launch_date": "December 25, 2021",
        "mission_type": "Space Observatory",
        "status": "Active",
        "objectives": "Observe distant galaxies, star systems, and exoplanets, with a focus on infrared observations.",
        "current_location": "Lagrange Point 2",
        "key_achievements": [
            "Most powerful space telescope ever built",
            "First direct image of an exoplanet",
            "Deepest infrared image of universe ever taken",
            "Detailed observations of early galaxy formation"
        ]
    },
    
    # Recent Chinese Missions
    "Chang'e 4": {
        "agency": "CNSA",
        "launch_date": "December 7, 2018",
        "mission_type": "Lander/Rover",
        "status": "Active",
        "objectives": "First soft landing on the far side of the Moon",
        "current_location": "Moon's far side",
        "key_achievements": [
            "First soft landing on lunar far side",
            "First plant growth experiment on Moon",
            "Discovery of gel-like substance in lunar crater",
            "Detailed analysis of lunar far side composition"
        ]
    },
    
    # Recent Indian Missions
    "Chandrayaan-2": {
        "agency": "ISRO",
        "launch_date": "July 22, 2019",
        "mission_type": "Orbiter/Lander/Rover",
        "status": "Partial success",
        "objectives": "Study the Moon's surface and measure lunar water ice.",
        "current_location": "Lunar orbit",
        "key_achievements": [
            "Successful orbiter deployment",
            "High-resolution mapping of lunar surface",
            "Detection of water molecules on lunar surface",
            "Study of lunar exosphere"
        ]
    }
}
# Route to serve the mission data
@app.route('/missions', methods=['GET'])
def get_missions():
    return jsonify(missions)

# Main route to render the frontend
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)