import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

export function NotFound() {
    return (
        <div className="dashboard-container">
            <div className="d-flex justify-content-center align-items-center" style={{ height: "100vh" }}>
                <div className="col-md-12 text-center">
                    <h1>404</h1>
                    <h2>Page Not Found</h2>
                    <p>Sorry, the page you are looking for does not exist.</p>
                </div>
            </div>
        </div>
    );
}