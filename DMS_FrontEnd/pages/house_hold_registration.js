import Head from 'next/head';
import Image from 'next/image';
import HouseHoldRegistrationImg from '../assets/images/houseHoldRegistration.png';

export default function HouseHoldRegistration() {
  return (
    <div>
      <Head>
        <title>DMS</title>
        <meta name="description" content="Household Registration" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <div>
          <div className="row">
            <div className="col-xm-12 col-lg-6 ">
              <div className="d-none  d-lg-block">
                <Image src={HouseHoldRegistrationImg} alt="Hero Image" />
              </div>
            </div>
            <div className="col-xm-12 col-lg-6">
              <div style={{ marginTop: '30%' }} className="container">
                <div className="mb-5 mt-5">
                  <h2 className="text-center">Household Registration</h2>
                </div>
                <div className="row">
                  <div className="col-6">
                    <div className="mb-3 ">
                      <label for="exampleFormControlInput1" className="form-label">
                        Head of family
                      </label>
                      <input type="text" className="form-control form-control-lg" id="exampleFormControlInput1" placeholder="full name" />
                    </div>
                  </div>
                  <div className="col-6">
                    <label for="exampleFormControlInput1" className="form-label">
                      --
                    </label>
                    <div className="mb-3">
                      <input type="text" className="form-control form-control-lg" id="exampleFormControlInput1" placeholder="phone number" />
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-6">
                    <div className="mb-3 ">
                      <label for="exampleFormControlInput1" className="form-label">
                        Son
                      </label>
                      <input type="text" className="form-control form-control-lg" id="exampleFormControlInput1" placeholder="full name" />
                    </div>
                  </div>
                  <div className="col-6">
                    <label for="exampleFormControlInput1" className="form-label">
                      --
                    </label>
                    <div className="mb-3">
                      <input type="text" className="form-control form-control-lg" id="exampleFormControlInput1" placeholder="phone number" />
                    </div>
                  </div>
                  <div className="col-6">
                    <div className="mb-3">
                      <input type="text" className="form-control form-control-lg" id="exampleFormControlInput1" placeholder="age" />
                    </div>
                  </div>
                  <div className="col-6">
                    <div className="mb-3">
                      <input type="text" className="form-control form-control-lg" id="exampleFormControlInput1" placeholder="condition" />
                    </div>
                  </div>
                </div>
                <div className="dropdown">
                  <button
                    className="btn btn-secondary dropdown-toggle"
                    type="button"
                    id="dropdownMenuButton"
                    data-toggle="dropdown"
                    aria-haspopup="true"
                    aria-expanded="false"
                  >
                    Add Occupants
                  </button>
                  <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <a className="dropdown-item" href="#">
                      Wife
                    </a>
                    <a class="dropdown-item" href="#">
                      Son
                    </a>
                    <a class="dropdown-item" href="#">
                      Daughter
                    </a>
                  </div>
                </div>
                <div className="d-grid gap-2 mt-5">
                  <button className="btn btn-success btn-lg" type="button">
                    Register
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
