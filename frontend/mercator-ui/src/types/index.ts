export interface Stat {
  visitId: string;
  web_domainName: string;
}

export interface RetreivedStat {
  visitId: string;
  domainName: string;
  crawlFinished: Number;
}
