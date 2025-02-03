import React, { useState } from "react";
import { Container, Row, Col, Nav } from "react-bootstrap";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"; // ✅ Import FontAwesome component
import { faTwitter, faFacebook, faInstagram } from "@fortawesome/free-brands-svg-icons"; // ✅ Import Icons

export default function Footer() {
  const [imageError, setImageError] = useState(false);

  return (
    <footer className="footer text-white py-4 d-flex flex-column" style={{ backgroundColor: "#333" }}>
      <Container>
        <Row className="align-items-start justify-content-center">
          {/* Logo Section */}
          <Col md={3} className="d-flex align-items-center justify-content-center">
            {imageError ? (
              <span className="fs-4">VolunTree</span>
            ) : (
              <img
                src="/voluntree_logo.png" // <-- Update this path to your actual logo
                alt="VolunTree Logo"
                width="200"
                className="me-2"
                onError={() => setImageError(true)}
              />
            )}
          </Col>

          {/* Navigation Links */}
          <Col md={3} className="mt-3 mt-md-0">
            <Nav className="flex-column">
              <Nav.Item>
                <Link to="/" className="footer-link text-white mb-1">Home</Link>
              </Nav.Item>
              <Nav.Item>
                <Link to="/organizations" className="footer-link text-white mb-1">Organizations</Link>
              </Nav.Item>
              <Nav.Item>
                <Link to="/volunteers" className="footer-link text-white mb-1">Volunteers</Link>
              </Nav.Item>
              <Nav.Item>
                <Link to="/events" className="footer-link text-white mb-1">Events</Link>
              </Nav.Item>
              <Nav.Item>
                <Link to="/tasks" className="footer-link text-white mb-1">Tasks</Link>
              </Nav.Item>
              <Nav.Item>
                <Link to="/login" className="footer-link text-white mb-1">Login</Link>
              </Nav.Item>
              <Nav.Item>
                <Link to="/signup" className="footer-link text-white mb-1">Sign Up</Link>
              </Nav.Item>
            </Nav>
          </Col>

          {/* Social Media Links */}
          <Col md={3} className="mt-3 mt-md-0">
            <Nav className="flex-column">
              <Nav.Item>
                <Nav.Link
                  href="https://twitter.com/VolunTree"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="footer-link text-white mb-1"
                >
                  <FontAwesomeIcon icon={faTwitter} className="me-2" /> @VolunTree
                </Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link
                  href="https://facebook.com/VolunTree"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="footer-link text-white mb-1"
                >
                  <FontAwesomeIcon icon={faFacebook} className="me-2" /> VolunTree
                </Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link
                  href="https://instagram.com/VolunTree"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="footer-link text-white"
                >
                  <FontAwesomeIcon icon={faInstagram} className="me-2" /> @VolunTree
                </Nav.Link>
              </Nav.Item>
            </Nav>
          </Col>
        </Row>

        {/* Footer Copyright */}
        <Row>
          <Col className="text-center mt-4">
            <small className="text-white-50">
              © {new Date().getFullYear()} VolunTree. All Rights Reserved.
            </small>
          </Col>
        </Row>
      </Container>
    </footer>
  );
}
