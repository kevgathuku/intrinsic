defmodule IntrinsicWeb.PageController do
  use IntrinsicWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end
end
