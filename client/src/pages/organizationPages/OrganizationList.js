import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { fetchData, deleteData } from "../../services/api";

export default function OrganizationList() {
    const [organizations, setOrganizations] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const itemsPerPage = 5;
    const [currentPage, setCurrentPage] = useState(1);

    useEffect(() => {
        async function getOrganizations() {
            setLoading(true);
            try {
                // ✅ Use the correct endpoint `/organizations` instead of `/organizations`
                const data = await fetchData("organizations");
                setOrganizations(data);
            } catch (err) {
                console.error("Error fetching organizations:", err);
                setError("Failed to fetch organizations. Please try again.");
            }
            setLoading(false);
        }
        getOrganizations();
    }, []);

    const totalPages = Math.ceil(organizations.length / itemsPerPage);
    const paginatedOrganizations = organizations.slice(
        (currentPage - 1) * itemsPerPage,
        currentPage * itemsPerPage
    );

    const handlePrevPage = () => {
        if (currentPage > 1) setCurrentPage(currentPage - 1);
    };

    const handleNextPage = () => {
        if (currentPage < totalPages) setCurrentPage(currentPage + 1);
    };

    const handleDelete = async (id) => {
        if (window.confirm("Are you sure you want to delete this organization?")) {
            await deleteData("organizations", id); // ✅ Correct API endpoint
            setOrganizations(organizations.filter(org => org.id !== id));
        }
    };

    return (
        <div className="container my-4">
            <h2 className="text-center mb-4">Organizations</h2>

            {loading ? <p>Loading...</p> : error ? <p className="text-danger">{error}</p> : (
                <>
                    <div className="row mb-3">
                        <div className="col">
                            <Link className="btn btn-primary me-3" to="/organizations/create">
                                Add New Organization
                            </Link>
                        </div>
                    </div>

                    <table className="table table-striped">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Contact Name</th>
                                <th>Phone</th>
                                <th>Email</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {paginatedOrganizations.map(org => (
                                <tr key={org.id}>
                                    <td>{org.id}</td>
                                    <td>{org.name}</td>
                                    <td>{org.contact_name}</td>
                                    <td>{org.contact_phone}</td>
                                    <td>{org.contact_email}</td>
                                    <td>
                                        <Link className="btn btn-warning btn-sm me-2" to={`/organizations/edit/${org.id}`}>
                                            Edit
                                        </Link>
                                        <button className="btn btn-danger btn-sm" onClick={() => handleDelete(org.id)}>
                                            Delete
                                        </button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>

                    <div className="d-flex justify-content-between">
                        <button className="btn btn-secondary" onClick={handlePrevPage} disabled={currentPage === 1}>
                            Previous
                        </button>
                        <span>Page {currentPage} of {totalPages}</span>
                        <button className="btn btn-secondary" onClick={handleNextPage} disabled={currentPage === totalPages}>
                            Next
                        </button>
                    </div>
                </>
            )}
        </div>
    );
}
