import Schedule from './Schedule';
import Bio from './Bio';
import Notebook from './Notebook';
import RequestedAppointments from './RequestedAppointments';
import Reviews from './Reviews';

function Me() {

  return (
    <div className="App, bg-primary">
      <header className="container-fluid">
        <h1 className="text-black">My Profile</h1>
        <h2 className="text-black">
          A place to see your own information
        </h2>
      </header>
        <div className="container">
            <div className="row justify-content-center">
                <div className="col-md-auto mh-100 mb-2">
                    <div className="card mh-100 bg-info border-dark" style={{width: '18rem'}}>
                        <div className="card-body overflow-auto">
                            <Schedule />
                        </div>
                    </div>
                </div>
                <div className="col-md-auto mh-100">
                    <div className="card mh-100 bg-info border-dark" style={{width: '36rem'}}>
                        <div className="card-body overflow-auto">
                            <Bio />
                        </div>
                    </div>
                </div>
            </div>
            <div className="row justify-content-center">
                <div className="col-md-auto mh-100 mb-2">
                    <div className="card mh-100 bg-info border-dark" style={{width: '18rem'}}>
                        <div className="card-body overflow-auto">
                            <RequestedAppointments />
                        </div>
                    </div>
                </div>
                <div className="col-md-auto mh-100">
                    <div className="card mh-100 bg-info border-dark" style={{width: '18rem'}}>
                        <div className="card-body overflow-auto">
                            <Reviews />
                        </div>
                    </div>
                </div>
                <div className="col-md-auto mh-100">
                    <div className="card mh-100 bg-info border-dark" style={{width: '18rem'}}>
                        <div className="card-body overflow-auto">
                            <Notebook />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
  );
}

export default Me;