import {useContextStore} from './ContextStore';

function Profiles() {
  const {count} = useContextStore()
  return (
    <div className="App">
      <header className="App-header">
        <h1>Profiles</h1>
        <h2>
          {`A place to see ${count} messages`} 
        </h2>
      </header>
    </div>
  );
}

export default Profiles;