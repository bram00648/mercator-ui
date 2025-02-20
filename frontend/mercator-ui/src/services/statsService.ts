import axios from "axios";
import { TechnologyStat } from "@/types";

// Use Vite environment variable properly
const API_BASE_URL = "http://localhost:5000/api/";

const fetchAllTechnologyStats = async (): Promise<TechnologyStat> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/stats/`);
    console.log(response.data);
    const data = response.data as TechnologyStat;

    // Transform the response data
    const transformedData: TechnologyStat = {
      visit_id: data.visit_id,
      detected_technologies: data.detected_technologies.map((tech) => ({
        name: tech.name,
      })),
    };

    return transformedData;
  } catch (error) {
    console.error("Error fetching technology stats:");
    throw error;
  }
};

const statsService = {
  fetchAllTechnologyStats,
};

export default statsService;
