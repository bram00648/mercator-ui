export async function fetchStats() {
    try {
      const response = await fetch("http://localhost:5000/api/stats");
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error("Error fetching stats:", error);
      return [];
    }
  }
  