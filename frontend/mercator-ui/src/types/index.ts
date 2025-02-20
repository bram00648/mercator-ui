export interface ApiResponse {
  visit_id: string;
  detected_technologies: string[];
}

export interface TechnologyStat {
  visit_id: string;
  detected_technologies: { name: string }[];
}
