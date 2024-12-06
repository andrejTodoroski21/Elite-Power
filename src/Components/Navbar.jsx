import { Link } from "react-router-dom";


function Navbar(){
    return(
        <nav>
            <Link to="/" id="title">Elite <a id="p">P</a>owe<a id="r">r</a></Link>
            <ul>
                <li>
                    <Link to="/about">About <span className="separator">|</span></Link>
                </li>
                <li>
                    <Link to="/services">Services <span className="separator">|</span></Link>
                </li>
                <li>
                    <Link to="/contact">Contact <span className="separator">|</span></Link>
                </li>
                <li>
                    <Link to="/program">Program</Link>
                </li>
            </ul>
        </nav>
    )
}
export default Navbar