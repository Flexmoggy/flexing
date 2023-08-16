import {useContextStore} from './ContextStore';

function Bio() {
  const {userDict, setUserDict} = useContextStore()
  console.log(userDict)
  return (
    <div className="bg-info" style={{height: '350px'}}>
      <header className="container-fluid text-center">
        <h1>Bio</h1>
        </header>
        <div className="container">
            <div className="row justify-content-left border-bottom border-dark">
                <div className="col-md-auto mh-25 mb-2" style={{width: '50%'}}>
                    <h3>Skills</h3>
                    <p>{userDict.skills}</p>
                </div>
                <div className="col-md-auto mh-25 mb-2" style={{width: '50%'}}>
                    <h3>Interests</h3>
                    <p>{userDict.interests}</p>
                </div>
            </div>
        </div>
        <div>
            <h3>About</h3>
            <p>{userDict.bio}</p>
        </div>
    </div>
  );
}

export default Bio;