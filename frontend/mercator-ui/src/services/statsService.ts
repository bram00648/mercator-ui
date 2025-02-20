import axios from "axios";
import { ApiResponse, TechnologyStat } from "@/types";

// Use Vite environment variable
const API_BASE_URL = process.env.VITE_APP_BASE_URL;

const fetchAllTechnologyStats = async (
  visit_id: number
): Promise<TechnologyStat> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/stats/`); // TODO: Add visitId filter later
    const data = response.data as TechnologyStat;

   
    const transformedData: TechnologyStat = {
      visit_id: data.visit_id, 
      detected_technologies: data.detected_technologies.map((tech) => ({
        name: tech.name,
      })), 
    };
    console.log(transformedData);
    return transformedData; 
  } catch (error) {
    console.error("Error fetching technology stats:", error);
    throw error; 
  }
};

const statsService = {
  fetchAllTechnologyStats,
};

export default statsService;
