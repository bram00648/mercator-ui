import axios from "axios";
import { RetreivedStat, Stat } from "@/types";

const API_BASE_URL = "http://localhost:5000/api";

const fetchAllStats = async (): Promise<Stat[]> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/stats/`);
    console.log(response.data);
    const data = response.data as Stat[];

    const transformedData: Stat[] = data.map((item) => ({
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

const fetchAllStatsByDomainName = async (
  domainName: string
): Promise<Stat[]> => {
  try {
    const response = await axios.get(
      `${API_BASE_URL}/stats/get_stats_by_domain_name`,
      {
        params: { domain_name: domainName },
      }
    );
    console.log(response.data);
    const data = response.data as Stat[];

    const transformedData: Stat[] = data.map((item) => ({
      visitId: item.visitId,
      web_domainName: item.web_domainName,
    }));

    return transformedData;
  } catch (error) {
    console.error("Error fetching technology stats by domain name:", error);
    throw error;
  }
};

const fetchAllStatsByVisitId = async (visitId: string): Promise<Stat[]> => {
  try {
    const response = await axios.get(
      `${API_BASE_URL}/stats/get_stats_by_visit_id`,
      {
        params: { visit_id: visitId },
      }
    );
    console.log(response.data);
    const data = response.data as Stat[];

    const transformedData: Stat[] = data.map((item) => ({
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
  fetchAllStats,
  fetchAllStatsByDomainName,
  fetchAllIdsAndDataByDomainName,
  fetchAllStatsByVisitId,
};

export default statsService;
