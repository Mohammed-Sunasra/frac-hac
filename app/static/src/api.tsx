const fetchAPI = async data => {
  try {
    const response = await fetch("/api/", {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    });
    const result = await response.json();
    return result;
  } catch (error) {
    throw error;
  }
};

export const fetchAnswer = async (pid: string, query: string) => {
  const queryData = { pid, query };
  const result = await fetchAPI(queryData);
  const { data } = result;
  return data;
};
