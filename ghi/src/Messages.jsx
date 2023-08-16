import {useContextStore} from './ContextStore';

function Messages() {
  const {count, setcount} = useContextStore()
  console.log(count)

  return (
    <div className="App">
      <header className="header">
        <h1>Messages</h1>
        <h2>
          {`A place ${count} for your messages!`}
        </h2>
      </header>
      <div>
        
      </div>
    </div>
  );
}

export default Messages;