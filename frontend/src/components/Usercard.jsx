export default function UserCard({ user }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: "10px", marginBottom: "10px" }}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
}
