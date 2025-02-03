import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { fetchData, deleteData } from "../../services/api";

export default function OrganizationList() {
    const [organizations, setOrganizations] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 5;

    // Fetch organizations from the server
    const getOrganizations = () => {
        fetchData("organizations")
            .then(data => {
                setOrganizations(data);
            })
            .catch(error => {
                console.error("Error fetching organizations:", error);
                alert("Unable to fetch organizations");
            });
    };

    useEffect(() => {
        getOrganizations();
    }, []);

    // Pagination logic
    const totalPages = Math.ceil(organizations.length / itemsPerPage);
    const paginatedOrganizations = organizations.slice(
        (currentPage - 1) * itemsPerPage,
        currentPage * itemsPerPage
    );

    const handlePrevPage = () => {
        if (currentPage > 1) {
            setCurrentPage(currentPage - 1);
        }
    };

    const handleNextPage = () => {
        if (currentPage < totalPages) {
            setCurrentPage(currentPage + 1);
        }
    };

    // Handle Delete
    const handleDelete = (id) => {
        if (window.confirm("Are you sure you want to delete this organization?")) {
            deleteData("organizations", id).then(() => getOrganizations());
        }
    };

    return (
        <div className="container my-4">
            <h2 className="text-center mb-4">Organizations</h2>

            <div className="row mb-3">
                <div className="col">
                    <Link
                        className="btn btn-primary me-3"
                        to="/organizations/create"
                    >
                        Add New Organization
                    </Link>
                </div>
            </div>

            <table className="table table-striped">
                <thead className="thead-dark">
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Contact Name</th>
                        <th>Contact Phone</th>
                        <th>Contact Email</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {paginatedOrganizations.length > 0 ? (
                        paginatedOrganizations.map((org, index) => (
                            <tr key={index}>
                                <td>{org.id}</td>
                                <td>{org.name}</td>
                                <td>{org.contact_name}</td>
                                <td>{org.contact_phone}</td>
                                <td>{org.contact_email}</td>
                                <td style={{ width: "10px", whiteSpace: "nowrap" }}>
                                    <Link
                                        className="btn btn-sm btn-warning me-2"
                                        to={`/organizations/edit/${org.id}`}
                                    >
                                        Edit
                                    </Link>
                                    <button
                                        className="btn btn-sm btn-danger"
                                        onClick={() => handleDelete(org.id)}
                                    >
                                        Delete
                                    </button>
                                </td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="6" className="text-center">No organizations found</td>
                        </tr>
                    )}
                </tbody>
            </table>

            {/* Pagination Controls */}
            <div className="d-flex justify-content-between align-items-center">
                <span>Page {currentPage} of {totalPages || 1}</span>
                <div>
                    <button
                        className="btn btn-secondary me-3"
                        onClick={handlePrevPage}
                        disabled={currentPage === 1}
                    >
                        &larr; Prev
                    </button>
                    <button
                        className="btn btn-secondary"
                        onClick={handleNextPage}
                        disabled={currentPage === totalPages}
                    >
                        Next &rarr;
                    </button>
                </div>
            </div>
        </div>
    );
}
