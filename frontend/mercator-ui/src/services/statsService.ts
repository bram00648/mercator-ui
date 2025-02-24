import axios from "axios";
import { RetreivedStat, TechnologyStat } from "@/types";

const API_BASE_URL = "http://localhost:5000/api";

const fetchAllTechnologyStats = async (): Promise<TechnologyStat[]> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/stats/`);
    console.log(response.data);
    const data = response.data as TechnologyStat[];

    const transformedData: TechnologyStat[] = data.map((item) => ({
      visitId: item.visitId,
      web_domainName: item.web_domainName,
    }));

    return transformedData;
  } catch (error) {
    console.error("Error fetching technology stats:", error);
    throw error;
  }
};

const fetchAllIdsAndDataByDomainName = async (
  domainName: string
): Promise<RetreivedStat[]> => {
  try {
    const response = await axios.get(
      `${API_BASE_URL}/stats/get_crawl_ids_by_domain_name`,
      {
        params: { domain_name: domainName },
      }
    );
    console.log(response.data);
    const data = response.data as RetreivedStat[];

    const transformedData: RetreivedStat[] = data.map((item) => ({
      visitId: item.visitId,
      domainName: item.domainName,
      crawlFinished: item.crawlFinished,
    }));

    return transformedData;
  } catch (error) {
    console.error("Error fetching technology stats by domain name:", error);
    throw error;
  }
};

const fetchAllTechnologyStatsByDomainName = async (
  domainName: string
): Promise<TechnologyStat[]> => {
  try {
    const response = await axios.get(
      `${API_BASE_URL}/stats/get_stats_by_domain_name`,
      {
        params: { domain_name: domainName },
      }
    );
    console.log(response.data);
    const data = response.data as TechnologyStat[];

    const transformedData: TechnologyStat[] = data.map((item) => ({
      visitId: item.visitId,
      web_domainName: item.web_domainName,
    }));

    return transformedData;
  } catch (error) {
    console.error("Error fetching technology stats by domain name:", error);
    throw error;
  }
};

const fetchAllTechnologyStatsByVisitId = async (
  visitId: string
): Promise<TechnologyStat[]> => {
  try {
    const response = await axios.get(
      `${API_BASE_URL}/stats/get_stats_by_visit_id`,
      {
        params: { visit_id: visitId },
      }
    );
    console.log(response.data);
    const data = response.data as TechnologyStat[];

    const transformedData: TechnologyStat[] = data.map((item) => ({
      visitId: item.visitId,
      web_domainName: item.web_domainName,
    }));

    return transformedData;
  } catch (error) {
    console.error("Error fetching technology stats by domain name:", error);
    throw error;
  }
};

const statsService = {
  fetchAllTechnologyStats,
  fetchAllTechnologyStatsByDomainName,
  fetchAllIdsAndDataByDomainName,
  fetchAllTechnologyStatsByVisitId,
};

export default statsService;
