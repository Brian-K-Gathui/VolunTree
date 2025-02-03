const BASE_URL = "http://localhost:5555";

export const fetchData = async (endpoint) => {
    try {
        const res = await fetch(`${BASE_URL}/${endpoint}`);
        if (!res.ok) {
            throw new Error(`Error ${res.status}: ${res.statusText}`);
        }
        return await res.json();
    } catch (error) {
        console.error("Fetch error:", error.message);
        return []; // Return an empty array to prevent crashes
    }
};

export const postData = async (endpoint, data) => {
    try {
        const res = await fetch(`${BASE_URL}/${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
        if (!res.ok) throw new Error(`Error ${res.status}: ${res.statusText}`);
        return await res.json();
    } catch (error) {
        console.error("Post error:", error.message);
    }
};

export const updateData = async (endpoint, id, data) => {
    try {
        const res = await fetch(`${BASE_URL}/${endpoint}/${id}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
        if (!res.ok) throw new Error(`Error ${res.status}: ${res.statusText}`);
        return await res.json();
    } catch (error) {
        console.error("Update error:", error.message);
    }
};

export const deleteData = async (endpoint, id) => {
    try {
        const res = await fetch(`${BASE_URL}/${endpoint}/${id}`, {
            method: "DELETE",
        });
        if (!res.ok) throw new Error(`Error ${res.status}: ${res.statusText}`);
    } catch (error) {
        console.error("Delete error:", error.message);
    }
};
