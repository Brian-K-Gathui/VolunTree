const BASE_URL = "http://localhost:5555";

export const fetchData = async (endpoint) => {
    const res = await fetch(`${BASE_URL}/${endpoint}`);
    return res.json();
};

export const postData = async (endpoint, data) => {
    const res = await fetch(`${BASE_URL}/${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });
    return res.json();
};

export const updateData = async (endpoint, id, data) => {
    const res = await fetch(`${BASE_URL}/${endpoint}/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });
    return res.json();
};

export const deleteData = async (endpoint, id) => {
    return fetch(`${BASE_URL}/${endpoint}/${id}`, { method: "DELETE" });
};
